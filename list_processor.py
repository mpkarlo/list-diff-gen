import gooeypie as gp
import csv


class GooeySetProcessor:
    """Offers a UI for performing set operations using Python's
        GooeyPie library."""

    def __init__(self):
        """Initialize GooeyPieApp, create UI elements and run app."""
        self.app = gp.GooeyPieApp("Gooey Set Processor")
        self.app.set_grid(3, 1)
        self.app.set_row_weights(1, 0, 1)
        self.app.width, self.app.height = 600, 800

        self.open_file_win = gp.OpenFileWindow(self.app, 'Open text file ...')
        self.open_file_win.set_initial_folder('Desktop')

        self._setup_input_ui()
        self._setup_ops_ui()
        self._setup_output_ui()

        self.app.run()

    def _setup_output_ui(self):
        # Add UI for output.
        self.output_container = gp.LabelContainer(self.app, 'Output')
        self.output_container.set_grid(1, 1)
        self.result_tbx = gp.Textbox(self.output_container)
        self.output_container.add(self.result_tbx, 1, 1, fill=True, stretch=True)
        self.app.add(self.output_container, 3, 1, fill=True, stretch=True)

    def _setup_ops_ui(self):
        # Add Container to group buttons that perform set ops.
        self.ops_container = gp.LabelContainer(self.app, 'Set Operations')
        self.ops_container.set_grid(1, 4)
        # Add button for union operation.
        self.set_union_btn = gp.Button(self.ops_container, '∪ ∙ UNION',
                                       lambda x: self._union(x))
        self.ops_container.add(self.set_union_btn, 1, 1, fill=True, stretch=True)
        # Add button for intersection operation.
        self.set_intersect_btn = gp.Button(self.ops_container, '∩ ∙ INTER',
                                           lambda x: self._intersect(x))
        self.ops_container.add(self.set_intersect_btn, 1, 2, fill=True, stretch=True)
        # Add button for difference of A - B operation.
        self.set_intersect_btn = gp.Button(self.ops_container, 'A - B ∙ DIFF',
                                           lambda x: self._diff_a(x))
        self.ops_container.add(self.set_intersect_btn, 1, 3, fill=True, stretch=True)
        # Add button for difference of B - A operation.
        self.set_intersect_btn = gp.Button(self.ops_container, 'B - A ∙ DIFF',
                                           lambda x: self._diff_b(x))
        self.ops_container.add(self.set_intersect_btn, 1, 4, fill=True, stretch=True)
        self.app.add(self.ops_container, 2, 1, fill=True, stretch=True)

    def _setup_input_ui(self):
        # Add Container to group input boxes.
        self.input_container = gp.LabelContainer(self.app, 'Input')
        self.input_container.set_grid(2, 4)
        self.input_container.set_row_weights(0, 1)
        self.input_container.set_column_weights(1, 0, 1, 0)

        # Create UI for file entry.
        self.set_a_inp = gp.Input(self.input_container)
        self.set_a_inp.disabled = True
        self.input_container.add(self.set_a_inp, 1, 1,
                                 valign='middle', fill=True)
        self.set_a_btn = gp.Button(self.input_container, 'Open ...',
                                   lambda e: self._open_file_a(e))
        self.input_container.add(self.set_a_btn, 1, 2, valign='middle')

        self.set_b_inp = gp.Input(self.input_container)
        self.set_b_inp.disabled = True
        self.input_container.add(self.set_b_inp, 1, 3,
                                 valign='middle', fill=True)
        self.set_b_btn = gp.Button(self.input_container, 'Open ...',
                                   lambda e: self._open_file_b(e))
        self.input_container.add(self.set_b_btn, 1, 4, valign='middle')

        # Create UI for set entry.
        self.set_a_tbx = gp.Textbox(self.input_container)
        self.input_container.add(self.set_a_tbx, 2, 1, fill=True,
                                 stretch=True, column_span=2)
        self.set_b_tbx = gp.Textbox(self.input_container)
        self.input_container.add(self.set_b_tbx, 2, 3, fill=True,
                                 stretch=True, column_span=2)

        # Add input_container to app.
        self.app.add(self.input_container, 1, 1, fill=True, stretch=True)

    def _union(self, event):
        """Perform the union of the sets of lines in both textboxes."""
        set_a = set(self.set_a_tbx.text.split('\n'))
        set_b = set(self.set_b_tbx.text.split('\n'))

        result_set = set_a.union(set_b)
        result_txt = '\n'.join(sorted(result_set))

        self.result_tbx.text = result_txt

    def _intersect(self, event):
        set_a = set(self.set_a_tbx.text.split('\n'))
        set_b = set(self.set_b_tbx.text.split('\n'))

        result_set = set_a.intersection(set_b)
        result_txt = '\n'.join(sorted(result_set))

        self.result_tbx.text = result_txt

    def _diff_a(self, event):
        set_a = set(self.set_a_tbx.text.split('\n'))
        set_b = set(self.set_b_tbx.text.split('\n'))

        result_set = set_a.difference(set_b)
        result_txt = '\n'.join(sorted(result_set))

        self.result_tbx.text = result_txt

    def _diff_b(self, event):
        set_a = set(self.set_a_tbx.text.split('\n'))
        set_b = set(self.set_b_tbx.text.split('\n'))

        result_set = set_b.difference(set_a)
        result_txt = '\n'.join(sorted(result_set))

        self.result_tbx.text = result_txt

    def _open_file_a(self, e):
        filepath = self.open_file_win.open()
        if filepath:
            try:
                with open(filepath, 'r') as file_obj:
                    csvreader = csv.reader(file_obj)
                    contents = [line[0] for line in csvreader]
            except FileExistsError or FileNotFoundError:
                pass
            else:
                self.set_a_inp.text = filepath
                self.set_a_tbx.text = '\n'.join(contents)

    def _open_file_b(self, e):
        filepath = self.open_file_win.open()
        if filepath:
            try:
                with open(filepath, 'r') as file_obj:
                    csvreader = csv.reader(file_obj)
                    contents = [line[0] for line in csvreader]
            except FileExistsError or FileNotFoundError:
                pass
            else:
                self.set_b_inp.text = filepath
                self.set_b_tbx.text = '\n'.join(contents)


if __name__ == '__main__':
    gp_app = GooeySetProcessor()
