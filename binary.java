import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class binary
{
    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new FileReader("binary.tex"))) {
            int character;
            
            while ((character = reader.read()) != -1) {
                System.out.print((char) character);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
