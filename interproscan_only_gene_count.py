import pandas as pd
import argparse

def count_unique_genes_by_InterPro_annotation(interproscan_file):
    interproscan_df = pd.read_excel(interproscan_file)

    # InterPro annotations 열에서 빈칸 또는 '-'로 표시된 행 제외
    interproscan_df = interproscan_df[interproscan_df['InterPro annotation'].apply(lambda x: str(x).strip() != '')]

    # 중복된 qseqid를 제거하여 유전자 개수 카운트
    unique_genes_count = interproscan_df['qseqid'].nunique()
    
    return unique_genes_count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count unique genes by InterPro annotations from the InterProScan output file.")
    parser.add_argument("--interproscan", required=True, help="Input file in Excel format containing InterProScan results.")
    args = parser.parse_args()

    result = count_unique_genes_by_InterPro_annotation(args.interproscan)
    print("InterPro annotation 기준 유전자 개수:", result)
