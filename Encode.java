import java.util.*;
public class Encode{

//args[0] is the first keyword, args[1] is the second keyword, args[2] is the desired message
  public static void main(String[] args) {
    secondstep( args[1], firststep(args[0], args[2]));
  }



// first step = polybius square
  public static String firststep(String keyword, String message){

    String result = "";

    keyword = keyword.toLowerCase();
    message = message.toLowerCase();

    char[] keywordChars = keyword.toCharArray();


    Map<Character,Integer> map = new HashMap<>();


 // this loop is removing repeat characters from the keyword.
 // repeat characters in the square would mess up the cipher
    String newkeyword = "";
    for(int i = 0; i < keyword.length(); i++){
      if(!map.containsKey(keywordChars[i]))
      {
        newkeyword += keywordChars[i];
        map.put(keywordChars[i], 1);
      }
    }


  // this loop is removing characters from the alphabet (and 0-9) that already appear in the modified keyword
  // this ensures duplicates aren't inserted into the square
    String alpha = "abcdefghijklmnopqrstuvwxyz0123456789";
    char[] alphaChars = alpha.toCharArray();
    String newAlpha = "";
    for(int i = 0; i < alpha.length(); i++){
      if(!map.containsKey(alphaChars[i])){
        newAlpha += alphaChars[i];
      }
    }

 // this loop extracts the two-letter code that each character in the ciphered text would map to in the square
    String grid = newkeyword + newAlpha;
    String key = "adfgvx";
    int pos = 0;
    for(int m = 0; m < message.length(); m++){
      pos = grid.indexOf(message.substring(m,m+1));
      result += "" + key.charAt(pos/6) + key.charAt(pos%6);
    }
    return result;

  }

// second step = columnar transposition
  public static void secondstep(String keyword, String part1){
  // I use TreeMap for this because tree map sorts alphabetically based on the key, rearranging the entries in the process
    Map<String,String> treeMap = new TreeMap<>();


    for(int i = 0; i < keyword.length(); i++){
      String temp = "";

    // this for loop makes a string out of individual characters that are a certain distance apart in the intermediate ciphered text
      for(int j = i; j < part1.length(); j+=keyword.length()){
        temp += ""+part1.charAt(j);
      }
      String tempKey = ""+keyword.charAt(i);


      if(treeMap.containsKey(""+keyword.charAt(i)))tempKey = ""+keyword.charAt(i)+i; // because TreeMap doesn't allow for repeats, I have to do this to allow for repeat characters in the second keyword

      treeMap.put(tempKey, temp);
    }

  // print out the cipher text
    for(Map.Entry<String, String> entry : treeMap.entrySet()){
      System.out.print(entry.getValue().toUpperCase() + " ");
    }
    System.out.println();

  }
}
