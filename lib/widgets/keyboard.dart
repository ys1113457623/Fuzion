import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:fuzion/controllers/chat_controller.dart';
import 'package:get/get.dart';

import '../models/speech_model.dart';

class KeyBoard extends StatefulWidget {
  KeyBoard({Key? key}) : super(key: key);

  @override
  State<KeyBoard> createState() => _KeyBoardState();
}

class _KeyBoardState extends State<KeyBoard> {
  bool isListening = false;
  String text = "";
  var textController = TextEditingController();

  ChatController controller = Get.put(ChatController());
  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.only(bottom: 20.h, left: 17.w, right: 18.w),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.all(
          Radius.circular(30.sp),
        ),
        color: const Color(0xFF3D4354),
      ),
      height: 50.h,
      // width: 327.w,

      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: <Widget>[
          SizedBox(
            width: 15.w,
          ),
          Expanded(
            // child: ImgUploadButton(),
            child: TextField(
              controller: textController,
              textInputAction: TextInputAction.search,
              onSubmitted: (value) async {
               await controller.addText(value);
               setState(() {
                 textController.clear();
               });
               await controller.run_code(value);

              },
              onChanged: (value) {
                setState(() {
                  print("A");
                  text = value;
                });
              },
              style: const TextStyle(color: Colors.white),
              autocorrect: false,
              decoration: InputDecoration(
                  hintText: "Ask something.....",
                  hintStyle: TextStyle(color: Colors.white),
                  border: InputBorder.none),
            ),
          ),
          SizedBox(
            width: 15.w,
          ),
          GestureDetector(
            onLongPress: toggleRecording,
            child: ClipOval(
              child: Container(
                decoration: BoxDecoration(
                    color: isListening
                        ? Colors.red.withOpacity(0.4)
                        : const Color(0xFF555E78),
                    shape: BoxShape.circle),
                width: 50.w,
                height: 50.h,
                child: !isListening
                    ? const Icon(Icons.mic)
                    : const Icon(
                        Icons.mic,
                        color: Colors.white,
                      ),
              ),
            ),
          )
        ],
      ),
    );
  }

  Future toggleRecording() async => SpeechApi.toggleRecording(

        onResult: ((text) {
          setState(() async {
            this.text = text;
            controller.addText(text);
            controller.run_code(text);
          });
          
        }),
        

        onListening: (isListening) {
          setState(() => this.isListening = isListening);

          if (!isListening) {
            Future.delayed(const Duration(seconds: 1), () {
              if (kDebugMode) {
                print(text);
              }
            });
          }
          
        },
      );
}
