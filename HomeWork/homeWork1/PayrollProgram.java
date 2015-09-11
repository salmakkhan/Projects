package homeWork1;

public class PayrollProgram {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	

		long hoursWorked = 40;
		double payRate = 10.0; 
		double taxRate = 0.10;
	
	System.out.println("Hours Worked : " + hoursWorked );
	System.out.println("pay Amount : " + (hoursWorked * payRate) );
	System.out.println("tax Amount : " + (hoursWorked * payRate * taxRate) );
	
	

	 /*long hoursWorked = 40;
	double payRate = 10.0;
	double taxRate = 0.10;
	
	System.out.println("Hours Worked : " + hoursWorked );
	System.out.println("pay Amount : " + (hoursWorked * payRate) );
	System.out.println("tax Amount : " + (hoursWorked * payRate * taxRate) );*/
		//The first try with the correct syntax 
	
	
	 	/*hoursWorked = 40;
		double payRate = 10.0;
		double taxRate = 0.10;
		
		System.out.println("Hours Worked : " + hoursWorked );
		System.out.println("pay Amount : " + (hoursWorked * payRate) );
		System.out.println("tax Amount : " + (hoursWorked * payRate * taxRate) );
		 //hoursWorked can not be run without a declaration*/
		
		
		 /*long hoursWorked ;
			double payRate = 10.0;
			double taxRate = 0.10;
			
			System.out.println("Hours Worked : " + hoursWorked );
			System.out.println("pay Amount : " + (hoursWorked * payRate) );
			System.out.println("tax Amount : " + (hoursWorked * payRate * taxRate) );*/
		
	//Local Variable hoursWorked was not initialized, hence the program didn't run. 	
	
	
	
	
	
	  
	}
}
