// n=4
// 11
// 21
// 22
// 31
// 32
// 33
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number : ");
        int n = sc.nextInt();
        // Outer loop controls rows
        for(int i=1; i<=3; i++){   // row values: 1,2,3
            // Inner loop controls columns
            for(int j=1; j<=i; j++){  // print up to row number
                System.out.println(i + "" + j);
                sc.close();
            }
        }
    }
}