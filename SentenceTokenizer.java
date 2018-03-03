//Author : Roman Ziserman

import java.io.*;
import java.util.Scanner;
import java.util.regex.Pattern;

/**
 * This class takes text files from a specified directory, removes a certain regex patterns, and creates new text
 * files sans all instances of the specified pattern.
 */

public class SentenceTokenizer {

    private File in_dir;
    private File out_dir;
    private String rm_pattern;

    /**
     *Constructor. Sets up the in and out directories, as well as the pattern to be removed.
     * @param in_dir
     * @param out_dir
     * @param pattern
     */
    SentenceTokenizer(String in_dir, String out_dir, String pattern) {
        this.in_dir = new File(in_dir);
        this.out_dir = new File(out_dir);
        this.rm_pattern = pattern;
    }

    //copy constructor
    public SentenceTokenizer(SentenceTokenizer copy){
        this.in_dir = copy.in_dir;
        this.out_dir = copy.out_dir;
        this.rm_pattern = copy.rm_pattern;
    }

    /**
     * This function loops over each file inside in_dir, writes to a new file with the same name as the input
     * file, and outputs it to out_dir.
     */
    public void transmorgrify(){
        try{
            Scanner in_file;
            BufferedWriter out_file;

            /*
            This loop iterates over each file in the list of files from in_dir.
             */
            for (File curr_file: in_dir.listFiles()){
                in_file = new Scanner(curr_file); //potential for IO error here
                String out_path = out_dir.getPath() + "\\" + curr_file.getName(); //For readability
                out_file = new BufferedWriter(new FileWriter(out_path));

                /*Now use a Scanner which creates tokens based on the delimiter pattern rm_pattern. Print the tokens to
                the corresponding file.
                 */
                in_file.useDelimiter(rm_pattern);
                while(in_file.hasNext()){
                    out_file.write(in_file.next());
                }

                /*
                Now close the scanner and the BufferedWriter for the next iteration.
                 */
                in_file.close();
                out_file.close();
            }
        } catch(IOException ioe){
            System.out.println("Something went wrong");
            ioe.printStackTrace();
        }
    }

    /*
    Buncha getters.
     */
    public String getIn_dir_path() {
        return in_dir.getPath();
    }

    public String getOut_dir_path() {
        return out_dir.getPath();
    }

    public String getRm_pattern() {
        return rm_pattern.toString();
    }
}
