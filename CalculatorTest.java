	public class CalculatorTest{

				
	 	public void testThatCalculatorCanAddTwoPositiveNumbers(){

		   int sum = Calculator.add(2,2);
		   int expectedSum = 4;
		
		   //assertion
		   if(sum!=4){
			System.err.printf("Test Failed\n Expected: %d\n Actual: %d", expectedSum, sum);
		  }else{
			System.out.println("Test Passed, yay :)");


		}

		
	}
			
		public static void main(String...args){
		 CalculatorTest CalculatorTest = new CalculatorTest();
		
		CalculatorTest.testThatCalculatorCanAddTwoPositiveNumbers();
	}
}