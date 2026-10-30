class Count{
    private double fuelMid;
    private double costFuelMid;
    private double annualMaleage;
    private double carInsurance;

    public Count(double fuelMid, double costFuelMid, double annualMaleage, double carInsurance){
        this.fuelMid = fuelMid;
        this.costFuelMid = costFuelMid;
        this.annualMaleage = annualMaleage;
        this.carInsurance = carInsurance;
    }
    public double count(){
        return fuelMid + costFuelMid + annualMaleage + carInsurance;
    }
    public static void Main(String[] args){
        Count BMW = new Count(200, 200, 123, 134);
        Console.WriteLine(BMW.count());
}}

    
    
