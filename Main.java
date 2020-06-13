package Tocadisco;

import java.util.ArrayList;
import java.util.Collections;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<Integer> a = new ArrayList<Integer>();
		
		a.add(70);
		a.add(80);
		a.add(90);
		/*a.add(90);
		a.add(30);
		a.add(60);*/
		 /*String t = "AEEDABDECBABDBB"
		  		+ "";
		  for(int i = 3; i <= t.length();i+=3)
			  System.out.println((i-2) +": " + t.charAt(i-3) + "\t" +
					  (i-1) + ": " + t.charAt(i-2)+ "\t" +
					  (i) + ": " + t.charAt(i-1)+ "\t" );
		  for(int i = t.length()%3; i >=0 ;i--)
			  System.out.print((t.length()-i) +": " + t.charAt(t.length()-i-1) + "\t");
		  System.out.println();*/
		System.out.println("FCFS");
		//fCFS(a, 50);
		System.out.println("S-CAM");
		//s_CAM(a, 170, 200);
		System.out.println("C-CAM");
		c_CAM(a, 80, 100);
		System.out.println("S-LOOK");
		s_LOOK(a, 170);
		System.out.println("C-LOOK");//SUELEN CONFUNDIRLO CON S-LOOK
		c_LOOK(a, 170);
		System.out.println("SSTF");
		sstf(a, 170);

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
