import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RouterIP {
    public static void main(String[] args) {
        try {
            // Execute the ipconfig /all command
            Process process = Runtime.getRuntime().exec("ipconfig");
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));

            String line;
            String defaultGateway = null;
            Pattern gatewayPattern = Pattern.compile("Default Gateway .*: (.*)");

            // Read the output line by line
            while ((line = reader.readLine()) != null) {
                Matcher gatewayMatcher = gatewayPattern.matcher(line);

                // Extract the default gateway IP address
                if (gatewayMatcher.find()) {
                    defaultGateway = gatewayMatcher.group(1).trim();
                }
            }

            reader.close();

            // Print the extracted information
            System.out.println("NextHop (Default Gateway) IP Address: " + defaultGateway);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}