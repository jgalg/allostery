#echo parm /home/hpc138/BPTI/EMIN/fl-1be9_free.prmtop [modi3] > dist_multi.in
#echo trajin fl-1be9_free.inpcrd parm [modi3] [modi33] >> dist_multi.in
#echo autoimage >> dist_multi.in

echo parm /home/kelly/PDZ/fl-1be9_free.prmtop [modi3] > dist_multi.in
echo trajin fl-1be9_free.inpcrd parm [modi3] [modi33] >> dist_multi.in
echo autoimage >> dist_multi.in

#for Amber12
#echo distance fl-1be9_free.inpcrd  :1 :1 out dist_multi.dat >> dist_multi.in

for i in $(seq 1 3); do 
    for j in $(seq 1 3  ); do
	if [ $i -lt $j ]; then
	    #for distance
	    #echo distance :$i :$j out dist_multi.dat >> dist_multi.in
	    echo nativecontacts :$i :$j writecontacts native.log out dist.dat mindist byresidue >> dist_multi.in
	fi
    done
done
