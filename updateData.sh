#/bin/sh

TOOL=geoclue-mlsdb-tool
FILE=../$1

COUNTRIES="Australia India"
REGIONS="Eastern_Europe Northern_Europe Western_Europe Southern_Europe"

for country in $COUNTRIES; do
 mkdir -p $country
 pushd $country
 $TOOL -c $country $FILE
 popd
done

for region in $REGIONS; do
 mkdir -p $region
 pushd $region
 $TOOL -r $region $FILE
 popd
done

