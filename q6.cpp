/* ## code to solve 2-SAT problem ##
   ## using depth-first search    ##
 */
#include <boost/config.hpp>
#include <iostream>
#include <vector>
#include <boost/graph/strong_components.hpp>
#include <boost/graph/adjacency_list.hpp>
#include <boost/foreach.hpp>

// need boost c/c++ library
// based on http://stackoverflow.com/questions/1733656/has-anyone-seen-a-2-sat-implementation
//   g++ -I /path/to/boost q6.cpp -o q6

//Properties of our graph. By default oriented graph
typedef boost::adjacency_list<> Graph;

int var_to_node(int var,int nb_vars)
{
    if(var < 0)
        return (-var + nb_vars);
    else
        return var;
}



int main(int argc, char * argv[])
{
  int nb_vars;
  FILE *fp;
  char line[100];
  int v1,v2,i;
  if (argc<2)
  {
    printf("!! enter filename!!\n");
    exit(1);
  }
  fp = fopen(argv[1],"r");
  if(fp==NULL)
  {
    printf("!! fail to open %s!!\n",argv[1]);
    exit(2);
  }
  fgets(line,100,fp);
  sscanf(line,"%d",&nb_vars);
  printf("Total %d nodes\n",nb_vars);
  //Creates a graph with twice as many nodes as variables
  Graph g(nb_vars * 2);
  while(fgets(line,100,fp)!=NULL)
  {
    sscanf(line,"%d %d",&v1,&v2);
    boost::add_edge(
                var_to_node(-v1,nb_vars),
                var_to_node(v2,nb_vars),
                g);
    boost::add_edge(
                var_to_node(-v2,nb_vars),
                var_to_node(v1,nb_vars),
                g);

  }
  fclose(fp);
  
  // Every node will belong to a strongly connected component
  std::vector<int> component(num_vertices(g));
  std::cout << strong_components(g, &component[0]) << std::endl;

    // Let's check if there is variable having it's negation
    // in the same SCC
    bool satisfied = true;
    for(i=0; i<nb_vars; i++)
    {
        if(component[i] == component[i+nb_vars])
          satisfied = false;
    }
    if(satisfied)
        std::cout << "Satisfied!" << std::endl;
    else
        std::cout << "Not satisfied!" << std::endl;
}
