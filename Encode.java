import java.util.*;
public class Encode{

//args[0] is the first keyword, args[1] is the second keyword, args[2] is the desired message
  public static void main(String[] args) {

    String part1 = grid(args[0], args[2]);
  }

  public static String grid(String keyword, String message){

    String result = "";

    keyword = keyword.toLowerCase();
    message = message.toLowerCase();

    char[] keywordChars = keyword.toCharArray();


    Map<Character,Integer> map = new HashMap<>();

    String newkeyword = "";
    for(int i = 0; i < keyword.length(); i++){
      if(!map.containsKey(keywordChars[i]))
      {
        newkeyword += keywordChars[i];
        map.put(keywordChars[i], 1);
      }
    }

    // System.out.println(newkeyword);


    String alpha = "abcdefghijklmnopqrstuvwxyz0123456789";
    char[] alphaChars = alpha.toCharArray();
    String newAlpha = "";

    for(int i = 0; i < alpha.length(); i++){
      if(!map.containsKey(alphaChars[i])){
        newAlpha += alphaChars[i];
      }
    }

    String grid = newkeyword + newAlpha;
    String key = "adfgvx";

    // System.out.println(grid);

    int pos = 0;
    for(int m = 0; m < message.length(); m++){
      pos = grid.indexOf(message.substring(m,m+1));
      result += "" + key.charAt(pos/6) + key.charAt(pos%6);
    }







    return result;

  }
}
