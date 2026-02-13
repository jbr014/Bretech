#!/usr/bin/env python3
import os
from urllib.request import Request, urlopen

IMAGES = {
    'hero.jpg': 'https://images.pexels.com/photos/4508751/pexels-photo-4508751.jpeg?auto=compress&cs=tinysrgb&h=900&w=1600&fit=crop',
    'service-1.jpg': 'https://images.pexels.com/photos/5050305/pexels-photo-5050305.jpeg?auto=compress&cs=tinysrgb&h=600&w=900&fit=crop',
    'service-2.jpg': 'https://images.pexels.com/photos/5408005/pexels-photo-5408005.jpeg?auto=compress&cs=tinysrgb&h=600&w=900&fit=crop',
    'service-3.jpg': 'https://images.pexels.com/photos/1624895/pexels-photo-1624895.jpeg?auto=compress&cs=tinysrgb&h=600&w=900&fit=crop',
    'office-1.jpg': 'https://images.pexels.com/photos/6804084/pexels-photo-6804084.jpeg?auto=compress&cs=tinysrgb&h=600&w=900&fit=crop',
    'service-4.jpg': 'https://images.pexels.com/photos/4818711/pexels-photo-4818711.jpeg?auto=compress&cs=tinysrgb&h=600&w=900&fit=crop',
    'team-1.jpg': 'https://images.pexels.com/photos/3182743/pexels-photo-3182743.jpeg?auto=compress&cs=tinysrgb&h=400&w=400&fit=crop',
    'team-2.jpg': 'https://images.pexels.com/photos/6914633/pexels-photo-6914633.jpeg?auto=compress&cs=tinysrgb&h=400&w=400&fit=crop',
    'team-3.jpg': 'https://images.pexels.com/photos/6592693/pexels-photo-6592693.jpeg?auto=compress&cs=tinysrgb&h=400&w=400&fit=crop',
}

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images')

def ensure_out_dir():
    os.makedirs(OUT_DIR, exist_ok=True)

def download(url, path):
    req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
    with urlopen(req) as r, open(path, 'wb') as f:
        data = r.read()
        f.write(data)

def main():
    ensure_out_dir()
    print('Downloading', len(IMAGES), 'images into', OUT_DIR)
    for name, url in IMAGES.items():
        out_path = os.path.join(OUT_DIR, name)
        try:
            print(' -', name)
            download(url, out_path)
        except Exception as e:
            print('   failed:', e)

    print('Done. Check assets/images/')

if __name__ == '__main__':
    main()
