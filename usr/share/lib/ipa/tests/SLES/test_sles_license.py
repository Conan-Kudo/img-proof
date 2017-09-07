def test_sles_license(host):
    license_dir = '/etc/YaST2/licenses/base'
    license_content = 'SUSE End User License Agreement'

    lic_dir = host.file(license_dir)
    if not lic_dir.exists:
        license_dir = '/etc/YaST2/licenses/SLES'
        lic_dir = host.file(license_dir)

    assert lic_dir.exists
    assert lic_dir.is_directory

    license = host.file(license_dir + '/license.txt')
    assert license.exists
    assert license.is_file
    assert license.contains(license_content)
