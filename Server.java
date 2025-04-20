import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Server {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(5000);
        System.out.println("Server started. Waiting for client...");

        Socket socket = serverSocket.accept();
        System.out.println("Client connected.");

        Scanner in = new Scanner(socket.getInputStream());
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

        while (true) {
            String operation = in.next();
            if (operation.equalsIgnoreCase("exit")) {
                System.out.println("Connection closed.");
                break;
            }

            double num1 = in.nextDouble();
            double num2 = in.nextDouble();
            double result = 0;

            switch (operation) {
                case "add":
                    result = num1 + num2;
                    break;
                case "sub":
                    result = num1 - num2;
                    break;
                case "mul":
                    result = num1 * num2;
                    break;
                case "div":
                    if (num2 != 0) result = num1 / num2;
                    else out.println("Cannot divide by zero");
                    break;
                default:
                    out.println("Invalid operation");
                    continue;
            }

            out.println("Result: " + result);
        }

        socket.close();
        serverSocket.close();
        in.close();
    }
}
