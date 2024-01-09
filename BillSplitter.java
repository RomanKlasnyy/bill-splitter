import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Random;

public class BillSplitter {
    public static void main(String[] args) {
        Map<String, Double> friends = new HashMap<>();
        boolean luckyFeature = false;
        String lucky = null;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the number of friends joining (including you):");
        int num = scanner.nextInt();
        System.out.println();

        if (num > 0) {
            System.out.println("Enter the name of every friend (including you), each on a new line:");
            for (int i = 0; i < num; i++) {
                String friend = scanner.next();
                friends.put(friend, 0.0);
            }
            System.out.println();
            System.out.println("Enter the total bill value:");
            double bill = scanner.nextDouble();
            System.out.println();
            System.out.println("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:");
            String answer = scanner.next();
            if (answer.equalsIgnoreCase("yes")) {
                System.out.println();
                lucky = (String) friends.keySet().toArray()[new Random().nextInt(friends.size())];
                System.out.println(lucky + " is the lucky one!");
                luckyFeature = true;
            } else {
                System.out.println();
                System.out.println("No one is going to be lucky");
            }
            double price;
            if (luckyFeature) {
                price = Math.round(bill / (friends.size() - 1) * 100.0) / 100.0;
            } else {
                price = Math.round(bill / friends.size() * 100.0) / 100.0;
            }
            System.out.println();
            for (Map.Entry<String, Double> entry : friends.entrySet()) {
                String name = entry.getKey();
                Double currentAmount = entry.getValue();
                if (!name.equals(lucky)) {
                    friends.put(name, currentAmount + price);
                }
            }
            System.out.println(friends);
        } else {
            System.out.println("No one is joining for the party");
        }
    }
}
