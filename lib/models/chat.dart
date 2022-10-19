class Chat {
  final List<Map<String, String>> chat;
  Chat({required this.chat});
  
  bool addResponse(String response) {
    try {
      int len = chat.length;
      chat[len - 1]['Bot'] = response;
      return true;
    } catch (e) {
      return false;
    }
  }

  
  bool addUserText(String text) {
    try {
      chat.add({'You': text});
      return true;
    } catch (e) {
      return false;
    }
  }  
  
  bool addLink(String text) {
    try {
      chat.add({'Link': text});
      return true;
    } catch (e) {
      return false;
    }
  }

  @override
  String toString() {
    String result = "";
    for (var i = 0; i < chat.length; i++) {
      result += '${chat[i]['You']!}\n';
      result += '${chat[i]['Bot']!}\n\n';
    }
    return result;
  }
}
