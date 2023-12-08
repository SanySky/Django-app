#для того чтобы данные выносились в файл, проверил наличие данных в самой таблице, скачал IDE для просмотра данного вида файлов, проверил правильность написания кода, спросил у одногрупников

import csv
from django.db.models.options import Options
from django.http import HttpResponse, HttpRequest
from django.db.models import QuerySet


class ExportAsCSVMixin:
    def export_csv(self, request: HttpRequest, queryset: QuerySet):
        meta: Options = self.model._meta
        field_names = (field.name for field in meta.fields)

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f"attachment; filename={meta}-export.csv"

        csv_writer = csv.writer(response)

        csv_writer.writerow(field_names)

        for obj in queryset:
            # TODO описали только то что вы сделали но не описали результат ваших действий
            # TODO туду принято писать там где предполагаемая проблема, не выходите за допуски по строке
            # TODO чтобы можно было ее прочитать
            # TODO как вы дебажели код ? покажите, что вам ответили в группе ?
            # TODO какие практические действия предприняли
            # TODO предположительно проблема в этой проанализируйте ее она записывает данные, что с ней не так ?
            csv_writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_csv.short_description = "Export for CSV"
