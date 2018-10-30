#!/bin/bash

name=$1
path_input=$2
type=$3
props_input=$4

path="../$path_input"

temp=${name:0:1}
componentName="${temp^^}"
flag=false
for (( i=1; i<${#name}; i++ )); do

    if [ "$flag" = true ]
    then
        flag=false
        temp=${name:$i:1}
        componentName+="${temp^^}"
        continue
    fi

    if [ "${name:$i:1}" != "-" ]
    then
        temp=${name:$i:1}
        componentName+="${temp}"
        
    else  
        flag=true
        continue
    fi

done

if [  ! -d "$path" ]; then
     echo $"ERROR: Source path  $path does not exist"
     exit 1 
fi

if [ ! -d "$path/$componentName" ]; then
  mkdir $path/$componentName
  
else 
    echo $"Error, there is an existing structure folder for $componentName"
     exit 1   
fi


proptypes_array=(`echo $props_input | sed 's/,/\n/g'`)
proptypes="$componentName.propTypes = {"
for prop_line in "${proptypes_array[@]}"
do
  prop=(`echo $prop_line | sed 's/\#/\n/g'`)
  props_tmp+=" ${prop[0]} ,"
  proptypes_tmp+="
  ${prop[0]}: PropTypes.${prop[1]},"
done
props=${props_tmp::-1}
proptypes+=${proptypes_tmp::-1}
proptypes+="
};"



case "$type" in
        class)
             bash CreateClassComponent.bash $componentName $name "$props" "$proptypes" $path 
            ;;
         
        stateless)
            bash CreateStatelessComponent.bash $componentName $name "$props" "$proptypes" $path 
            ;;
         
        pure)
            bash CreatePureComponent.bash $componentName $name "$props" "$proptypes" $path 
            ;;         
        *)
            echo $"Usage: $0 {class|stateless|pure}"
            exit 1
esac

bash CreateSCCSFile.bash $componentName $name $path
bash CreateTestFile.bash $componentName $path
bash CreateIndex.bash $componentName $path
