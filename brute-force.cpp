#include <iostream>
#include <vector>

using namespace std;

void print(vector<char> &input)
{
    for (int i = 0; i < input.size(); i++)
    {
        cout << input.at(i);
    }
    cout << endl;
}

int power(int number,int exponent)
{
	int index;
	int result = 1;
	for (index = 0;index < exponent;index++)
	{
			result*=number;
	}
	return result;
}

int reset(int indices[],int increment_position,int repeat,int all_characters)
{
	if (indices[increment_position] >= all_characters)
	{
		indices[increment_position] = 0;
		indices[increment_position-1] += 1;
		if (increment_position > 0)
		{
			increment_position -= 1;
			reset(indices,increment_position,repeat,all_characters);
		}
		else
		{
			increment_position = all_characters-1;
			return 0;
		}
	}
	return 0;
}

int fill(char characters[],char combination[],int indices[],int combination_position,int increment_position,int repeat,int all_characters)
{
    int i;
	combination[combination_position] = characters[indices[combination_position]];
	if (combination_position > 0)
	{
		combination_position -= 1;
		fill(characters,combination,indices,combination_position,increment_position,repeat,all_characters);
	}
	else
	{
        vector<char> combination_generated;
		for (i = 0;i < repeat;i++)
		{
			//printf("%c",combination[i]);
            combination_generated.push_back(combination[i]);
		}
		//printf("\n");
        print(combination_generated);
        combination_generated.clear();
		indices[increment_position] += 1;
		reset(indices,increment_position,repeat,all_characters);
	}
}

int generate(char characters[],int repeat,int all_characters)
{
	int indices[repeat];
	char combination[repeat];
	int combination_position = repeat - 1;
	int increment_position = repeat - 1;
	int i;
	for (i=0;i<repeat;i++)
	{
		indices[i] = 0;
	}
	for (i = 0; i < power(all_characters,repeat); i++)
	{
		fill(characters,combination,indices,combination_position,increment_position,repeat,all_characters);
	}
	return 0;
}

int main()
{
	char characters[62] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
						   'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
						   '0','1','2','3','4','5','6','7','8','9'};
	int all_characters = 62;
	int repeat = 6;
	while (1)
	{
		generate(characters,repeat,all_characters);
		repeat++;
	}
}
