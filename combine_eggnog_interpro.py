import pandas as pd
import argparse

def count_genes_by_GO(interproscan_file, eggnog_file):
    interproscan_df = pd.read_excel(interproscan_file)
    eggnog_df = pd.read_excel(eggnog_file)

    interproscan_df['GO annotations'] = interproscan_df['GO annotations'].apply(lambda x: x if isinstance(x, str) else '')
    eggnog_df['GOs'] = eggnog_df['GOs'].apply(lambda x: x if isinstance(x, str) else '')

    interproscan_df['GO annotations'] = interproscan_df['GO annotations'].fillna('')
    eggnog_df['GOs'] = eggnog_df['GOs'].fillna('')

    non_empty_genes_by_GO_interproscan = interproscan_df[interproscan_df['GO annotations'].apply(lambda x: x.strip() != '')]['qseqid'].nunique()
    non_empty_genes_by_GO_eggnog = eggnog_df[eggnog_df['GOs'].apply(lambda x: x.strip() != '-')]['query'].nunique()

    combined_df = pd.concat([interproscan_df, eggnog_df], ignore_index=True, sort=False)
    combined_df['GO annotations'] = combined_df['GO annotations'].fillna('')
    combined_df['GOs'] = combined_df['GOs'].fillna('')

    non_empty_genes_combined = combined_df[combined_df['GO annotations'].apply(lambda x: x.strip() != '') | combined_df['GOs'].apply(lambda x: x.strip() != '-')]['qseqid'].nunique()

    return non_empty_genes_by_GO_interproscan, non_empty_genes_by_GO_eggnog, non_empty_genes_combined

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Interproscan과 eggnog의 GO annotations를 결합하고 유전자 수를 세는 프로그램")
    parser.add_argument("--interpro", type=str, help="interproscan 결과가 담긴 Excel 파일 경로")
    parser.add_argument("--eggnog", type=str, help="eggnog 결과가 담긴 Excel 파일 경로")
    args = parser.parse_args()

    interproscan_result, eggnog_result, combined_result = count_genes_by_GO(args.interpro, args.eggnog)

    print("Interproscan에서 GO annotations로 기록된 유전자 수:", interproscan_result)
    print("Eggnog에서 GOs로 기록된 유전자 수:", eggnog_result)
    print("중복되지 않은 유전자 총 개수:", combined_result)
