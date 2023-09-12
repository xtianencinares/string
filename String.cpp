#include <iostream>
#include <fstream>
using namespace std;
main()
{
       ifstream encinares ("input.txt");
       string str;
      
       while (getline(encinares,str))
      {
      cout<<str<<endl;
      
            }
      system("pause");
            }
