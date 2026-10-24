using System;

class Amount {
    private object[] equipment;
    private int quantityDays;
    private bool insurance;

    public Amount(object[] equipment, int quantityDays, bool insurance) {
        this.equipment = equipment;
        this.quantityDays = quantityDays;
        this.insurance = insurance;
    }
    
    public double count(object[] equipment, int days){
        return (int)equipment[1] * days; 
    }
    public override string ToString(){
        return "Equip: " + equipment[0] +" , "+ equipment[1] +", Days: "+ quantityDays +", Insuranse: "+ insurance + ";";
    }
    public static void Main(){
        Amount amount1 = new Amount(new object[] {"snowboard", 250}, 12, true);
        Console.WriteLine(amount1.count(new object[] {"snowboard", 250}, 12));

        Console.WriteLine(amount1.ToString());
    }

}