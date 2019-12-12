package CSVJAVA;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.ObjectOutputStream;
import java.util.List;
import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.io.FileReader;
import java.io.FileWriter;
public class SpendingDust {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<String> list1 = new ArrayList<String>();
		List<String> list2 = new ArrayList<String>();
		List<String> list3 = new ArrayList<String>();
		List<String> list4 = new ArrayList<String>();
		List<String> card1 = new ArrayList<String>();
		List<String> card2 = new ArrayList<String>();
		List<String> card3 = new ArrayList<String>();
		List<String> card4 = new ArrayList<String>();
		List<String> card5 = new ArrayList<String>();
		List<String> card6 = new ArrayList<String>();
		List<String> card7 = new ArrayList<String>();
		List<String> card8 = new ArrayList<String>();
		List<String> out=new ArrayList<String>();
		String[] Str=null;
		try {
			String file="/home/swcu/Desktop/CSVJAVA/dust.txt";
			BufferedReader br=new BufferedReader(new InputStreamReader(new FileInputStream(file),"euc-kr"));
			String cur=null;
			while((cur=br.readLine())!=null) {
				Str=null;
				Str=cur.split("\t");
				for(int i=0; i<Str.length; i++) {
					Str[i]=Str[i].trim();
				}
				list1.add(Str[0]);
				list2.add(Str[1]);
				list3.add(Str[2]);
				list4.add(Str[3]);
			}
			
			String file2="/home/swcu/Desktop/CSVJAVA/card.txt";
			BufferedReader br2=new BufferedReader(new InputStreamReader(new FileInputStream(file2),"euc-kr"));
			String cur2=null;
			while((cur2=br2.readLine())!=null) {
				Str=null;
				Str=cur2.split("\t");
				for(int i=0; i<Str.length; i++) {
					Str[i]=Str[i].trim();
				}
				card1.add(Str[0]);
				card2.add(Str[1]);
				card3.add(Str[2]);
				card4.add(Str[3]);
				card5.add(Str[4]);
				card6.add(Str[5]);
				card7.add(Str[6]);
				card8.add(Str[7]);
			}
			out.add(card1.get(0)+"\t"+card2.get(0)+"\t"+card4.get(0)+"\t"
					+card5.get(0)+"\t"+card6.get(0)+"\t"+card7.get(0)+"\t"+card8.get(0)+"\t"
					+list3.get(0)+"\t"+list4.get(0));
			for(int i=1; i<list1.size(); i++) {
				for(int j=1; j<card1.size(); j++) {
					if(card2.get(j).equals("350") && list2.get(i).equals("350") && card1.get(j).equals(list1.get(i))) {
						out.add(card1.get(j)+"\t"+card2.get(j)+"\t"+card4.get(j)+"\t"
					+card5.get(j)+"\t"+card6.get(j)+"\t"+card7.get(j)+"\t"+card8.get(j)+"\t"
					+list3.get(i)+"\t"+list4.get(i));
					}
				}
			}
			String[] outArray=out.toArray(new String[out.size()]);
			try(FileWriter fout= new FileWriter("/home/swcu/Desktop/CSVJAVA/Spending+Dust.txt")) {
			    PrintWriter pout = new PrintWriter(fout);
			    for( String line:outArray ) {
			        pout.println(line);
			    }
			}
		}catch(IOException e) {
			e.getStackTrace();
		}		
	}
}
