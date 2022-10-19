import 'package:fuzion/models/chat.dart';
import 'package:get/get.dart';

class ChatController extends GetxController {
  Rx<Chat> chat = Chat(chat: []).obs;
  RxBool contextNeeded = false.obs;
  RxBool lastMsgWasImage = false.obs;

  void addImageLink(String link) {
    chat.value.addUserText(link);
    update();
    lastMsgWasImage.update((val) {
      val = true;
    });
  }

  void addText(String text) {
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
      // call the api here
      String response = "Some text from bot";
      // after getting the response
      chat.value.addResponse(response);
      update();
    }
  }
}
