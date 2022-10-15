import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:fuzion/widgets/keyboard.dart';

class TextScreen extends StatelessWidget {
  const TextScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xff1C1F2A),
      body: SingleChildScrollView(
        child: Column(
          children: [
            SizedBox(
              height: 30.h,
            ),
            Padding(
              padding: EdgeInsets.symmetric(horizontal: 16.sp),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Container(
                    child: Image.asset("assets/arrow.png"),
                    decoration: BoxDecoration(
                        color: Color(0xFF555E78), shape: BoxShape.circle),
                    width: 50.w,
                    height: 50.h,
                  ),
                  Container(
                    child: Image.asset(
                      "assets/profile.png",
                      fit: BoxFit.contain,
                    ),
                    decoration: BoxDecoration(
                        color: Color(0xFF555E78), shape: BoxShape.circle),
                    width: 50.w,
                    height: 50.h,
                  )
                ],
              ),
            ),
            SizedBox(
              height: 20.h,
            ),
            Padding(
              padding: EdgeInsets.all(18.sp),
              child: Align(
                alignment: Alignment.topRight,
                child: Container(
                  child: Padding(
                    padding: EdgeInsets.all(8.sp),
                    child: Text(
                      "Meditation app ui ideas for daily routine",
                      textAlign: TextAlign.left,
                      style: TextStyle(
                          color: Colors.white,
                          fontSize: 15.sp,
                          fontWeight: FontWeight.w500),
                    ),
                  ),
                  width: 260.w,
                  height: 65.h,
                  decoration: BoxDecoration(
                      color: Color(0xFF7169E2),
                      borderRadius: BorderRadius.only(
                          topLeft: Radius.circular(16.sp),
                          bottomLeft: Radius.circular(16.sp),
                          topRight: Radius.circular(16.sp))),
                ),
              ),
            ),
            Padding(
              padding: EdgeInsets.all(18.sp),
              child: Align(
                alignment: Alignment.topLeft,
                child: Container(
                  child: Padding(
                    padding: EdgeInsets.all(8.sp),
                    child: Text(
                      "Here are images for suggested query",
                      textAlign: TextAlign.left,
                      style: TextStyle(
                          color: Colors.white,
                          fontSize: 15.sp,
                          fontWeight: FontWeight.w500),
                    ),
                  ),
                  width: 260.w,
                  height: 65.h,
                  decoration: BoxDecoration(
                      color: Color(0xFF3D4354),
                      borderRadius: BorderRadius.only(
                          bottomLeft: Radius.circular(16.sp),
                          bottomRight: Radius.circular(16.sp),
                          topRight: Radius.circular(16.sp))),
                ),
              ),
            ),
            Container(
              width: 325.w,
              height: 310.h,
              decoration: BoxDecoration(
                  color: Color(0xFF3D4354),
                  borderRadius: BorderRadius.all(Radius.circular(16.sp))),
            ),
            SizedBox(
              height: 20.h,
            ),
            Padding(
              padding: EdgeInsets.all(18.sp),
              child: Align(
                alignment: Alignment.topRight,
                child: Container(
                  child: Padding(
                    padding: EdgeInsets.all(8.sp),
                    child: Text(
                      "Meditation app tagline ideas for daily routine, use it for tracking stress, prayer and many tasks.",
                      textAlign: TextAlign.left,
                      style: TextStyle(
                          color: Colors.white,
                          fontSize: 15.sp,
                          fontWeight: FontWeight.w500),
                    ),
                  ),
                  width: 282.w,
                  height: 75.h,
                  decoration: BoxDecoration(
                      color: Color(0xFF7169E2),
                      borderRadius: BorderRadius.only(
                          topLeft: Radius.circular(16.sp),
                          bottomLeft: Radius.circular(16.sp),
                          topRight: Radius.circular(16.sp))),
                ),
              ),
            ),
            KeyBoard()
          ],
        ),
      ),
    );
  }
}
//
// class _MessageTile extends StatelessWidget {
//   const _MessageTile(
//       {Key? key, required this.message, required this.messageData})
//       : super(key: key);
//
//   final String message;
//   final String messageData;
//   static const _br = 26.0;
//   @override
//   Widget build(BuildContext context) {
//     return Padding(
//       padding: EdgeInsets.symmetric(vertical: 4),
//       child: Align(
//         alignment: Alignment.centerLeft,
//         child: Column(
//           mainAxisSize: MainAxisSize.min,
//           crossAxisAlignment: CrossAxisAlignment.start,
//           children: [
//             Container(
//               decoration: BoxDecoration(
//                   color: Theme.of(context).cardColor,
//                   borderRadius: BorderRadius.only(
//                     topLeft: Radius.circular(_br),
//                     topRight: Radius.circular(_br),
//                     bottomRight: Radius.circular(_br),
//                   )),
//               child: Padding(
//                 padding: EdgeInsets.symmetric(horizontal: 12, vertical: 20),
//                 child: Text(message),
//               ),
//             ),
//             Padding(
//               padding: EdgeInsets.only(top: 8.0),
//               child: Text(
//                 messageData,
//                 style: TextStyle(
//                   color: Colors.red,
//                   fontSize: 10,
//                   fontWeight: FontWeight.bold,
//                 ),
//               ),
//             ),
//           ],
//         ),
//       ),
//     );
//   }
// }
//
// class _MessageOwnTile extends StatelessWidget {
//   const _MessageOwnTile(
//       {Key? key, required this.message, required this.messageData})
//       : super(key: key);
//
//   final String message;
//   final String messageData;
//   static const _br = 26.0;
//   @override
//   Widget build(BuildContext context) {
//     return Padding(
//       padding: EdgeInsets.symmetric(vertical: 4),
//       child: Align(
//         alignment: Alignment.centerRight,
//         child: Column(
//           mainAxisSize: MainAxisSize.min,
//           crossAxisAlignment: CrossAxisAlignment.end,
//           children: [
//             Container(
//               height: 50.h,
//               width: 249.w,
//               decoration: const BoxDecoration(
//                   color: Color(0xFF7169E2),
//                   borderRadius: BorderRadius.only(
//                     topLeft: Radius.circular(_br),
//                     bottomRight: Radius.circular(_br),
//                   )),
//               child: Padding(
//                 padding: EdgeInsets.symmetric(horizontal: 12, vertical: 20),
//                 child: Text(message),
//               ),
//             ),
//             Padding(
//               padding: EdgeInsets.only(top: 8.0),
//               child: Text(
//                 messageData,
//                 style: const TextStyle(
//                   color: Colors.red,
//                   fontSize: 10,
//                   fontWeight: FontWeight.bold,
//                 ),
//               ),
//             ),
//           ],
//         ),
//       ),
//     );
//   }
// }
