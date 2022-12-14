import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

class SplashScreen extends StatelessWidget {
  const SplashScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xff1C1F2A),
      body: Padding(
        padding: EdgeInsets.symmetric(vertical: 50.h),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Image.asset("assets/robot.png"),
            SizedBox(
              height: 40.h,
            ),
            Text(
              "How may i help\n you today",
              textAlign: TextAlign.center,
              style: TextStyle(
                fontWeight: FontWeight.w500,
                fontSize: 33.sp,
                color: Colors.white,
              ),
            ),
            SizedBox(
              height: 80.h,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                Container(
                  decoration: const BoxDecoration(
                      color: Color(0xFF555E78), shape: BoxShape.circle),
                  width: 50.w,
                  height: 50.h,
                  child: Image.asset("assets/micro.png"),
                ),
                Container(
                  decoration: const BoxDecoration(
                      color: Color(0xFF555E78), shape: BoxShape.circle),
                  width: 50.w,
                  height: 50.h,
                  child: Image.asset("assets/Vector.png"),
                )
              ],
            )
          ],
        ),
      ),
    );
  }
}
