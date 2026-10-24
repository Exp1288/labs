using System;
using System.Collections.Generic;

public class Drink {
    private String type;
    private double amount;
    private Dictionary<String, int> recAmount;

    public Drink(String type, double amount){
        this.type = type;
        this.amount = amount;
        this.recAmount = new Dictionary<string, int>(StringComparer.OrdinalIgnoreCase) {
            { "Пиво", 330},
            { "Вино", 150},
            {"Водка", 50}
    };    }
    public void checkRecomendedAmount(){
        Console.WriteLine("Введите название напитка: ");
        String name = Console.ReadLine();
        Console.WriteLine("Введите количество выпитого в мл: ");
        int b = int.Parse(Console.ReadLine());
        if (this.recAmount.TryGetValue(name, out int recommended)) {
            if (b > recommended) {
                Console.WriteLine("Больше нормы");
            } 
            else if (b < recommended) {
                Console.WriteLine("Слишком мало"); 
            } 
            else {
                Console.WriteLine("Доза в норме");
            }
        } 
        else {
                Console.WriteLine($"Пользователь или напиток '{name}' не найден.");
        }
    }
    public static void Main(){
        Drink me = new Drink("Водка", 30);
        me.checkRecomendedAmount();
    }
}