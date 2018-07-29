if [ "$#" -lt 1 ]
then
    echo "usage:"
    echo "./quick.sh numplayers [eik]"
    exit 1
fi
opt=$2
if [ -z $2 ]
then
    opt=eik
fi
optarr=(`echo $opt | grep -o .`)
end=0
if [ $1 -gt 2 ]
then
    end=1
fi
if [ $1 -gt 3 ]
then
    end=2
fi
nums=(1 3 4)
for inum in `seq 0 $end`
do
    for iopt in "${optarr[@]}"
    do
	decks="${iopt}${nums[$inum]} ${decks}"
    done
done
echo python3 setup.py $1 7 7 $opt $decks
python3 setup.py $1 7 7 $opt $decks
