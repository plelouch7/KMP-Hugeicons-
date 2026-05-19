import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")

def convert_svg_to_vd(svg_path, vd_path):
    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()

        # Get dimensions from viewBox or width/height
        viewbox = root.attrib.get('viewBox', '0 0 24 24').split()
        if len(viewbox) == 4:
            vw, vh = viewbox[2], viewbox[3]
        else:
            vw = root.attrib.get('width', '24').replace('px', '')
            vh = root.attrib.get('height', '24').replace('px', '')

        vd_root = ET.Element('vector', {
            'xmlns:android': 'http://schemas.android.com/apk/res/android',
            'android:width': f'{vw}dp',
            'android:height': f'{vh}dp',
            'android:viewportWidth': vw,
            'android:viewportHeight': vh
        })

        # Global attributes
        g_fill = root.attrib.get('fill', 'none')
        g_stroke = root.attrib.get('stroke', 'none')
        g_stroke_width = root.attrib.get('stroke-width', '1.5')
        g_stroke_linecap = root.attrib.get('stroke-linecap', 'round')
        g_stroke_linejoin = root.attrib.get('stroke-linejoin', 'round')

        for elem in root.iter():
            tag = elem.tag.split('}')[-1]
            if tag == 'path':
                d = elem.attrib.get('d')
                if d:
                    path_attribs = {'android:pathData': d}

                    fill = elem.attrib.get('fill', g_fill)
                    stroke = elem.attrib.get('stroke', g_stroke)
                    stroke_width = elem.attrib.get('stroke-width', g_stroke_width)
                    stroke_linecap = elem.attrib.get('stroke-linecap', g_stroke_linecap)
                    stroke_linejoin = elem.attrib.get('stroke-linejoin', g_stroke_linejoin)

                    if fill != 'none':
                        path_attribs['android:fillColor'] = '#FF000000'
                    if stroke != 'none':
                        path_attribs['android:strokeColor'] = '#FF000000'
                        path_attribs['android:strokeWidth'] = stroke_width
                        path_attribs['android:strokeLineCap'] = stroke_linecap
                        path_attribs['android:strokeLineJoin'] = stroke_linejoin

                    ET.SubElement(vd_root, 'path', path_attribs)

            elif tag == 'circle':
                cx = elem.attrib.get('cx', '0')
                cy = elem.attrib.get('cy', '0')
                r = elem.attrib.get('r', '0')
                # Simplified circle to path conversion isn't easy here,
                # but VectorDrawable supports group/clip or we can try to use a placeholder.
                # For most icons, they use path. If circle is used, we might need more logic.
                pass

        # Write to file
        with open(vd_path, 'w', encoding='utf-8') as f:
            f.write(prettify(vd_root))
        return True
    except Exception as e:
        print(f"Error converting {svg_path}: {e}")
        return False

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    folder = os.path.join(base_dir, 'composeApp/src/commonMain/composeResources/drawable')
    backup_folder = os.path.join(base_dir, 'svg_backups')

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    print(f"Processing icons in {folder}...")
    count = 0
    for filename in os.listdir(folder):
        if filename.endswith('.svg'):
            svg_file = os.path.join(folder, filename)
            vd_file = os.path.join(folder, filename.replace('.svg', '.xml'))
            if convert_svg_to_vd(svg_file, vd_file):
                # Move original to backup
                os.rename(svg_file, os.path.join(backup_folder, filename))
                count += 1

    print(f"Successfully converted {count} icons.")

if __name__ == "__main__":
    main()
