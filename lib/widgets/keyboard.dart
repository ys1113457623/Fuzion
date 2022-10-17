import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

class KeyBoard extends StatelessWidget {
  const KeyBoard({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.all(
          Radius.circular(30.sp),
        ),
        color: Color(0xFF3D4354),
      ),
      height: 50.h,
      width: 327.w,
      child: Row(
        children: <Widget>[
          SizedBox(
            width: 15.w,
          ),
          Expanded(
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
          ClipOval(
            child: Container(
              child: Image.asset("assets/micro.png"),
              decoration: BoxDecoration(
                  color: Color(0xFF555E78), shape: BoxShape.circle),
              width: 50.w,
              height: 50.h,
            ),
          )
        ],
      ),
    );
  }
}
