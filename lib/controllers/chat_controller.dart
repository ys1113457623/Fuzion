import 'dart:convert';

import 'package:fuzion/models/chat.dart';
import 'package:get/get.dart';
import 'package:http/http.dart' as http;

class ChatController extends GetxController {
  Rx<Chat> chat = Chat(chat: []).obs;
  RxBool contextNeeded = false.obs;
  RxBool lastMsgWasImage = false.obs;
  RxBool lastSpoken = false.obs;

  Future<void> run_code(String text) async {
    print(text);
    var headers = {
      'Content-Type': 'application/json',
      'Authorization':'Bearer ',
    };

    var data =
        '{"model": "text-davinci-002", "prompt": "$text", "temperature": 0, "max_tokens": 1500}';
//parse URI
    Uri url = Uri.parse('https://api.openai.com/v1/completions');
    var res = await http.post(url, headers: headers, body: data);
    if (res.statusCode != 200) {
      throw Exception('http.post error: statusCode= ${res.statusCode}');
    }

    //parse res.body as Map
    Map<String, dynamic> res2 =
        Map<String, dynamic>.from(json.decode(res.body));
    String result = res2['choices'][0]['text'];
    chat.value.addResponse(result);
    update();

  }

  void addImageLink(String link) {
    chat.value.addUserText(link);
    update();
    lastMsgWasImage.update((val) {
      val = true;
    });
  }

  Future<void> addText(String text) async {
    chat.value.addUserText(text);
    update();
    if (contextNeeded.value) {
      Map<String, String> data = {"query": chat.toString()};

      // call the api here
      String response = "Some text from bot";
      // after getting the response
      chat.value.addResponse(response);
      update();
    } else {
      Map<String, String> data = {"query": text};
      if (lastMsgWasImage.value) {
        data.addAll({
          "link": chat.value.chat.last['Link']!,
        });
      }
      update();
      // call the api here

      // after getting the response

    }
  }
}
