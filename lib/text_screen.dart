import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:flutter_staggered_grid_view/flutter_staggered_grid_view.dart';
import 'package:fuzion/widgets/keyboard.dart';

class TextScreen extends StatelessWidget {
  const TextScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    var text = "Some text from user";
    return Scaffold(
      backgroundColor: const Color(0xff1C1F2A),
      body: SingleChildScrollView(
        child: Container(
          height:812.h ,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const TopButton(),
              Column(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  
                  Column(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      
                   
                      UserInputText(text: text),
                      ReplyFromBot(text: text),
                      ClipRRect(
                        borderRadius: BorderRadius.all(Radius.circular(16.sp),),
                        
                        child: Container(
                          width: 325.w,
                          height: 310.h,
                          
                          decoration: const BoxDecoration(
                              color: Color(0xFF3D4354),
                      ),


                        ),
                      ),
                      SizedBox(
                        height: 20.h,
                      ),
                      UserInputText(text: text),
                    ],
                  ),
                  const KeyBoard()
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class TopButton extends StatelessWidget {
  const TopButton({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: () {
        Navigator.pop(context);
      },
      child: Padding(
                padding: EdgeInsets.symmetric(horizontal: 16.sp,vertical: 40.h),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container(
                      decoration: const BoxDecoration(
                          color: Color(0xFF555E78), shape: BoxShape.circle),
                      width: 50.w,
                      height: 50.h,
                      child: Image.asset("assets/arrow.png"),
                    ),
                    
                  ],
                ),
              ),
    );
  }
}

class ReplyFromBot extends StatelessWidget {
  const ReplyFromBot({
    Key? key,
    required this.text,
  }) : super(key: key);

  final String text;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.all(18.sp),
      child: Align(
        alignment: Alignment.topLeft,
        child: Container(

          constraints:                const BoxConstraints(minWidth: 100, maxWidth: 282),

          decoration: BoxDecoration(
              color: const Color(0xFF3D4354),
              borderRadius: BorderRadius.only(
                  bottomLeft: Radius.circular(16.sp),
                  bottomRight: Radius.circular(16.sp),
                  topRight: Radius.circular(16.sp))),
          child: Padding(
            padding: EdgeInsets.all(8.sp),
            child: Text(
text,
              textAlign: TextAlign.left,
              style: TextStyle(
                  color: Colors.white,
                  fontSize: 15.sp,
                  fontWeight: FontWeight.w500),
            ),
          ),
        ),
      ),
    );
  }
}

class UserInputText extends StatelessWidget {
  const UserInputText({
    Key? key,
    required this.text,
  }) : super(key: key);

  final String text;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(18.sp),
      child: Align(
        alignment: Alignment.topRight,
        child: Container(
          constraints:
              const BoxConstraints(minWidth: 100, maxWidth: 282),
          // height: 75.h,
          padding: EdgeInsets.all(7.sp),
          decoration: BoxDecoration(
              color: const Color(0xFF7169E2),
              borderRadius: BorderRadius.only(
                  topLeft: Radius.circular(16.sp),
                  bottomLeft: Radius.circular(16.sp),
                  topRight: Radius.circular(16.sp))),
          child: Text(
text,
            textAlign: TextAlign.left,
            style: TextStyle(
                color: Colors.white,
                fontSize: 15.sp,
                fontWeight: FontWeight.w500),
          ),
        ),
      ),
    );
  }
}
