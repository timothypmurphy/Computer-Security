import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

import javax.xml.bind.DatatypeConverter;

import java.io.*;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class hashes {

	static List<String> encryptedPass = new ArrayList<>();
	public static PrintWriter writer;
	static boolean firstLoop = true;
	static PrintWriter hashes;
	static PrintWriter words;
	static MessageDigest md;

	public static void main(String[] args) throws IOException {

		HashMap<String, String> passwords = new HashMap<String, String>();
		
		File file = new File("rockyou-samples.md5.txt");
		
		BufferedReader br = new BufferedReader(new FileReader(file));
		
    	try {
			hashes = new PrintWriter("hashes.txt", "UTF-8");
	    	words = new PrintWriter("words.txt", "UTF-8");
		} catch (FileNotFoundException | UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		try {
			md = MessageDigest.getInstance("MD5");

		} catch (NoSuchAlgorithmException e){
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		 String st; 
		  while ((st = br.readLine()) != null) 
		    encryptedPass.add(st); 
		  

		char[] alphabet = new char[] { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
				'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' };

		possibleStrings(3, alphabet,"");
		
		hashes.close();
		words.close();
		
}
	
    public static void possibleStrings(int maxLength, char[] alphabet, String curr) {

    	String hash;


    	
	        if(curr.length() == maxLength) {


	        	md.update(curr.getBytes());
	        	hash = DatatypeConverter.printHexBinary(md.digest()).toLowerCase();
	        	if(encryptedPass.contains(hash)) {
	        		words.println(curr);
	        		hashes.println(hash);
	        	}
				System.out.println(curr);

	        } else {
	            for(int i = 0; i < alphabet.length; i++) {
	                String oldCurr = curr;
	                curr += alphabet[i];
	                possibleStrings(maxLength,alphabet,curr);
	                curr = oldCurr;
	            }
	        }

    	
        // If the current string has reached it's maximum length


        // Else add each letter from the alphabet to new strings and process these new strings again

    }
	
}
