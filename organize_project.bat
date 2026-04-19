@echo off
REM Reorganization script for Python workspace

echo Creating directory structure...
mkdir projects 2>nul
mkdir learning 2>nul
mkdir assets 2>nul
mkdir assets\weights 2>nul
mkdir projects\tomato-disease-ai 2>nul
mkdir learning\basics 2>nul

echo Moving projects...
if exist "TwitterLocationAI" move "TwitterLocationAI" "projects\twitter-location-ai"
if exist "increase video quality" move "increase video quality" "projects\video-enhancer"

echo Moving learning materials...
if exist "sllybus" move "sllybus" "learning\syllabus"
if exist "A to Z Python" move "A to Z Python" "learning\a-to-z-course"
if exist "class code" move "class code" "learning\class-notes"
if exist "my code" move "my code" "learning\personal-practice"
if exist "dsa_practice.py" move "dsa_practice.py" "learning\dsa_practice.py"
if exist "DSA_Tracker.md" move "DSA_Tracker.md" "learning\DSA_Tracker.md"
if exist "Palindrome.py" move "Palindrome.py" "learning\basics\Palindrome.py"

echo Moving individual files...
if exist "app.py" move "app.py" "projects\tomato-disease-ai\app.py"
if exist "hey.py" move "hey.py" "projects\tomato-disease-ai\train.py"
if exist "TomatoLeafAI.ipynb" move "TomatoLeafAI.ipynb" "projects\tomato-disease-ai\exploration.ipynb"
if exist "modal1.ipynb" move "modal1.ipynb" "projects\tomato-disease-ai\model_v1.ipynb"
if exist "hello_world.py" move "hello_world.py" "learning\basics\hello_world.py"
if exist "mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5" move "mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5" "assets\weights\mobilenet_v2_base.h5"

echo Organization complete!
pause
