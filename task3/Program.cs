using System;

public class Aging{
    private int age;

    public Aging(int age){
        this.age = age;
    }
    public void ageCheck(){
        if (this.age > 18){
            Console.WriteLine("You're minor");
            Console.WriteLine("Enjoy your childhood while u could");
        }
        else if (this.age >= 18 && this.age <= 20){
            Console.WriteLine("You're adolescent");
            Console.WriteLine("You're cooked");
        }
        else {
            Console.WriteLine("You're an adult");
            Console.WriteLine("Just die bro");
        }
    }

    public static void Main(){
        Aging me = new Aging(18);
        me.ageCheck();
    }

}