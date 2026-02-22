import java.util.Scanner;
class ctimer
{
 void marathi()
 {
   System.out.println("exam started in marathi language");
   int i;
   for (i = 60; i >= 1; i--) 
   {
   System.out.print(i + " ");
   }
 }
 void english()
 {
   System.out.println("exam started in english language");
 }
 void hindi()
 {
   System.out.println("exam started in hindi language");
 }
 public static void main(String ar[])
 {
   char ch;
   Scanner s=new  Scanner(System.in);
   ctimer obj=new ctimer();
   System.out.println("Select language for exam\nM-marathi\nE-english\nH-hindi");
   ch=s.next().charAt(0);
   switch(ch)
   {
    case 'M':
    obj.marathi();
    break;
    case 'E':
    obj.english();
    break;
    case 'H':
    obj.hindi();
    break;
   }
 }
}