import java.net.InetAddress;
import java.net.UnknownHostException;

public class HostIP {
    public static void main(String[] args) {
        try {
            InetAddress ip = InetAddress.getLocalHost();
            String hostname = ip.getHostName();
            System.out.println("Your current IP address : " + ip);
            System.out.println("Your current Hostname : " + hostname);
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }
}