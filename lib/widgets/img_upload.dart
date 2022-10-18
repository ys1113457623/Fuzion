import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/container.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:get/get.dart';

import '../controllers/imgupload_controller.dart';

class ImgUploadButton extends GetView<ImgUploadController> {
  ImgUploadButton({
    Key? key,
  }) : super(key: key) {
    Get.put(ImgUploadController());
  }

  @override
  Widget build(BuildContext context) {
    return TextButton(
      onPressed: () async {
        print("button pressed");
        controller.pickimagefromgallery();
      },
      child: const Text(
        "Upload Image",
        style: TextStyle(
          fontSize: 16,
        ),
      ),
    );
  }
}
