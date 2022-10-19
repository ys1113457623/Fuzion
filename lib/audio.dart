import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

class AudioScreen extends StatelessWidget {
  const AudioScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF1C1F2A),
      body: Padding(
        padding: EdgeInsets.all(20.sp),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Image.asset("assets/image 3.png"),
            Text(
              "Ask Something...",
              style: TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.w500,
                  fontSize: 25.sp),
            ),
            Container(
              decoration: const BoxDecoration(
                  color: Color(0xFF555E78), shape: BoxShape.circle),
              width: 50.w,
              height: 50.h,
              child: Image.asset("assets/micro.png"),
            ),
          ],
        ),
      ),
    );
  }
}
