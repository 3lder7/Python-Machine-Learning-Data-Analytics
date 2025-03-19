conjunto_a={1,2}
conjunto_b={3,4}
conjunto_a.union(conjunto_b)#{1,2,3,4}

conjunto_c={1,2,3}
conjunto_d={2,3,4}
conjunto_c.intersection(conjunto_d)#{2,3}

conjunto_e={1,2,3}
conjunto_f={2,3,4}
conjunto_e.difference(conjunto_f)#{1}
conjunto_f.difference(conjunto_e)#{4}


conjunto_g={1,2,3}
conjunto_h={2,3,4}
conjunto_g.symmetric_difference(conjunto_h)#{1,4}

conjunto_i={1,2,3}
conjunto_j={4,1,2,5,6,3}
conjunto_i.issubset(conjunto_j) #false 
conjunto_j.issubset(conjunto_i) #true #todos os elementos de J estão em I

