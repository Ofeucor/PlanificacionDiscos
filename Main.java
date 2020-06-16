import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;


public class Main {

	public static final Scanner teclado = new Scanner(System.in);

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<Integer> a = new ArrayList<Integer>();
		System.out.println("Introduce punto inicial:");
		int origen = teclado.nextInt();
		System.out.println("Introduce el tamaño:");
		int tam = teclado.nextInt();
		createArray(a);
		menu(origen, a, tam);

	}

	public static void menu(int origen, ArrayList<Integer> a, int tam){

		int opt;
		do{
			System.out.println("0. Salida\n1. FCFS\n2. S-CAM\n3. C-CAM\n4. S-LOOK\n5. C-LOOK\n5. SSTF\n");
			switch(opt = teclado.nextInt()){
				case 1:
					System.out.println("FCFS");
					fCFS(a, origen);
					break;
				case 2:
					System.out.println("S-CAM");
					s_CAM(a, origen, tam);
					break;
				case 3:
					System.out.println("C-CAM");
					c_CAM(a, origen, tam);
					break;
				case 4:
					System.out.println("S-LOOK");
					s_LOOK(a, origen);
					break;
				case 5:
					System.out.println("C-LOOK");//SUELEN CONFUNDIRLO CON S-LOOK
					c_LOOK(a, 170);
					break;
				case 6:
					System.out.println("SSTF");
					sstf(a, 170);
					break;
				case 0:
					break;
			}
		}while(opt != 0);

	}

	public static void createArray(ArrayList<Integer> a){
		int n;
		do{
			System.out.print("Pulsa '-1' para terminar o introduce la siguiente parada:");
			a.add((n = teclado.nextInt()));
		}while(n != -1);
	}
	
	public static void fCFS(ArrayList<Integer> a, int origen) {
		int d = 0;
		while(!a.isEmpty()) {
			d += Math.abs((origen-a.get(0)));
			origen = a.get(0);
			a.remove(0);
		}
		System.out.println("Distancia: " + d);
	}
	
	public static void s_CAM(ArrayList<Integer> a, int origen, int tam) {
		a.add(origen);
		Collections.sort(a);
		int d = 0;
		d += (tam-origen);
		d += (tam-a.get(0));
		System.out.println("Distancia: " + d);
	}
	
	public static void c_CAM(ArrayList<Integer> a, int origen, int tam) {
		a.add(origen);
		Collections.sort(a);
		int d = 0;
		int p0 = a.indexOf(origen);
		d += (2*tam-origen);
		d += a.get(p0-1);
		System.out.println("Distancia: " + d);
	}
	
	public static void s_LOOK(ArrayList<Integer> a, int origen) {
		a.add(origen);
		int p0 = a.indexOf(origen);
		Collections.sort(a);
		int d = 0;
		d += (a.get(a.size()-1)-origen);
		if(p0 != 0) 
			d += a.get(a.size()-1) - a.get(0);
		System.out.println("Distancia: " + d);
	}
	
	public static void c_LOOK(ArrayList<Integer> a, int origen) {
		a.add(origen);
		Collections.sort(a);
		int p0 = a.indexOf(origen);
		int d = 0;
		d += (a.get(a.size()-1)-origen);
		if(p0 != 0) 
			d += a.get(p0-1) - a.get(0);
		System.out.println("Distancia: " + d);
	}
	
	public static void sstf(ArrayList<Integer> a, int origen) {
		int d = 0;
		while(!a.isEmpty()) {
			System.out.print(origen + "  ");
			int nw = nearleast(a, origen);
			d += Math.abs((origen-a.get(nw)));
			origen = a.get(nw);
			a.remove(nw);
		}
		System.out.println("\nDistancia: " + d);

		
	}
	
	public static int nearleast(ArrayList<Integer> a, int origen) {
		int d = 100000;
		int t=-1;
		for(int i = 0; i < a.size(); i++) {
			if(Math.abs((a.get(i)-origen)) < d) {
				t = i;
				d = Math.abs(a.get(i)-origen);

			}
		}
		return t;
		
	}

}
