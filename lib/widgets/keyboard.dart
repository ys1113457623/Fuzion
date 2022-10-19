import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

import '../models/speech_model.dart';

class KeyBoard extends StatefulWidget {
  const KeyBoard({Key? key}) : super(key: key);

  @override
  State<KeyBoard> createState() => _KeyBoardState();
}

class _KeyBoardState extends State<KeyBoard> {
  String text = 'Press the button and start speaking';
  bool isListening = false;
  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.only(bottom: 20.h),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.all(
          Radius.circular(30.sp),
        ),
        color: const Color(0xFF3D4354),
      ),
      height: 50.h,
      width: 327.w,
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: <Widget>[
          SizedBox(
            width: 15.w,
          ),
          const Expanded(
            // child: ImgUploadButton(),
            child: TextField(
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

  Future toggleRecording() => SpeechApi.toggleRecording(
        onResult: (text) => setState(() => this.text = text),
        onListening: (isListening) {
          setState(() => this.isListening = isListening);

          if (!isListening) {
            Future.delayed(const Duration(seconds: 1), () {
              print(text);
            });
          }
        },
      );
}
