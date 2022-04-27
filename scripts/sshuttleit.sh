mkdir -p /home/jc/web/static/larger
cd /home/jc/projects/Real-ESRGAN/
python3 inference_realesrgan.py -n RealESRGAN_x4plus -i /home/jc/web/static/ -s 8 -o /home/jc/web/static/larger/
cd /home/jc/web/static/larger/
scp -P 1981 * jc@104.131.43.222:projects/nonhumanworks/web/static/
rm -rf /home/jc/web/static/*
