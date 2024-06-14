from unstructured.partition.pdf import partition_pdf

class PdfExtractorSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PdfExtractorSingleton, cls).__new__(cls)
            cls._instance.init(*args, **kwargs)
        return cls._instance




    def init(self, pdf_file_path, image_output_directory):
        self.elements = partition_pdf(
            filename=pdf_file_path,
            strategy="hi_res",
            extract_images_in_pdf=True,
            extract_image_block_types=["Image"],
            extract_image_block_to_payload=False,
            extract_image_block_output_dir=image_output_directory,
            infer_table_structure=True,
            starting_page_number=True)

    def get_elements(self):
        return self.elements



