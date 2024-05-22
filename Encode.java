import java.util.*;
public class Encode{

//args[0] is the first keyword, args[1] is the second keyword, args[2] is the desired message
  public static void main(String[] args) {

    String part1 = grid(args[0], args[2]);
  }

  public static String grid(String keyword, String message){

    String result = "";
    char[][] square = new char[6][6];
    char[] messageChars = message.toCharArray();


    Map<Character,Integer> map = new HashMap<>();

    String newMessage = "";
    for(int i = 0; i < message.length(); i++){
      if(!map.containsKey(messageChars[i]))
      {
        newMessage += messageChars[i];
        map.put(messageChars[i], 1);
      }
    }

    System.out.println(newMessage);







    return result;

  }
}
