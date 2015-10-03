swig -javascript -node -c++ vabamorf.i
python createbinding.py > binding.gyp
node-gyp configure
node-gyp build
