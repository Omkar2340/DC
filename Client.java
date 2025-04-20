import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("localhost", 5000);
        System.out.println("Connected to server.");

        Scanner scanner = new Scanner(System.in);
        Scanner in = new Scanner(socket.getInputStream());
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

        while (true) {
            System.out.print("Enter operation (add, sub, mul, div) or 'exit': ");
            String operation = scanner.next();
            if (operation.equalsIgnoreCase("exit")) {
                out.println("exit");
                break;
            }

            System.out.print("Enter first number: ");
            double num1 = scanner.nextDouble();

            System.out.print("Enter second number: ");
            double num2 = scanner.nextDouble();

            out.println(operation + " " + num1 + " " + num2);
            String response = in.nextLine();
            System.out.println("Server: " + response);
        }

        socket.close();
        scanner.close();
        in.close();
    }
}
