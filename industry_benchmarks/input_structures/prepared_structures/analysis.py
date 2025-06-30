import os

import boto3


start_directory = '.'
print(f"Starting search in: {os.path.abspath(start_directory)}")

# os.walk yields a 3-tuple: (dirpath, dirnames, filenames)
for dirpath, dirnames, filenames in os.walk(start_directory):
    # We only care about PDB files
    pdb_files = [f for f in filenames if f.endswith(".pdb")]
    if not pdb_files:
        continue

    # Check if the directory is at the desired depth (e.g., 'AAA/BBB')
    # We split the path by the OS separator and count the parts.
    # A path like './AAA/BBB' will have 3 parts.
    path_parts = dirpath.split(os.sep)
    if len(path_parts) == 3: # Corresponds to './level1/level2'
        for pdb_file in pdb_files:
            _, target, protein = dirpath.split('/')
            try:
                s3_client.download_file("exs-centaur-dev", f"zwu/industry_out/md_ready/{target}_{protein}_DU_0/receptor_{target}_{protein}_DU_0.bss", f"{target}/{protein}/protein.bss")
            except:
                print(f"{target},{protein}")


print("\n--- Search complete ---")