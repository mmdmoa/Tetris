echo "Blacking main.py ..."
black *py
echo "\nBlacking core/*py ..."
black core/*py
echo "\nBlacking core/common/*py ..."
black core/common/*py
