class aa
{
 void sum(int...value)
 {
  int ttl=0;
  for(int i:value)
  {
   ttl=ttl+i;
  }
   System.out.println(ttl);
 }
 static public void main(String arr[])
 {
  aa obj=new aa();
  obj.sum(3,4,5,3,3,4,3,3,4);
 }
}
