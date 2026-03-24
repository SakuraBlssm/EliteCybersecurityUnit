package SakuraBadIncryption;
import java.util.Scanner;
import java.lang.Math;

public class Main {
    private static String characters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*(){}[]':;,<.>/?_-+=|~ "; //pray that this contains every character
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        //user input
        System.out.print("Enter what to encrypt: ");
        String toEncrypt = input.nextLine();

        System.out.print("Enter the desired key: ");
        String userKey = input.nextLine();

        input.close(); //stop yelling at me to close this

        //Incrypts (tm) and decrypts the messages
        String encrypted = Encrypt(toEncrypt, userKey);
        String decrypted = Decrypt(encrypted, userKey);
        System.out.println(encrypted);
        System.out.println(decrypted);
    }

    public static String Encrypt(String toEncrypt, String userKey) {
        String encrypted = "";

        for (int ind = 0; ind <= toEncrypt.length() - 1; ind++) {
            String character = toEncrypt.substring(ind, ind + 1);

            int charInd = GetCharacterIndex(character);
            if (charInd == -1) {
                System.out.println("WARNING: character " + character + " lost!");
                continue;
            }
            
            int keyLetter = ind % userKey.length();
            int keyInd = GetCharacterIndex(userKey.substring(keyLetter, keyLetter + 1));

            charInd = Math.abs((charInd + keyInd) - characters.length());

            encrypted += characters.substring(charInd, charInd + 1);
        }

        return encrypted;
    }

    //decrypts the message to at least be somewhat legible
    public static String Decrypt(String encrypted, String userKey) {
        String decrypted = "";

        for (int ind = 0; ind <= encrypted.length() - 1; ind++) {
            String character = encrypted.substring(ind, ind + 1);
            
            int charInd = GetCharacterIndex(character);
            int keyLetter = ind % userKey.length();
            int keyInd = GetCharacterIndex(userKey.substring(keyLetter, keyLetter + 1));
            
            charInd = -charInd - keyInd + characters.length(); //WARNING: i have insufficient IQ to convert symbols back so they become letters
            
            if (charInd == -1) {
                System.out.println("WARNING: character " + character + " lost!");
                continue;
            }
            
            decrypted += characters.substring(charInd, charInd + 1);
            System.out.println(characters.substring(charInd, charInd + 1) + ": " + charInd);
        }

        return decrypted;
    }

    public static int GetCharacterIndex(String character) {
        for (int i = 0; i <= characters.length() - 1; i++) {
            String fromCharList = characters.substring(i, i + 1);

            if (fromCharList.equals(character)) {
                return i;
            }
        }
        
        System.out.println("not found");
        return -1;
    }
}